// in src/restClient
import {
    GET_LIST,
    GET_ONE,
    GET_MANY,
    GET_MANY_REFERENCE,
    CREATE,
    UPDATE,
    DELETE,
    fetchUtils,
} from 'admin-on-rest';
import markdown from 'markdown';
const API_URL = window.location.origin  + '/api';

/**
 * @param {String} type One of the constants appearing at the top if this file, e.g. 'UPDATE'
 * @param {String} resource Name of the resource to fetch, e.g. 'posts'
 * @param {Object} params The REST request params, depending on the type
 * @returns {Object} { url, options } The HTTP request parameters
 */
const convertRESTRequestToHTTP = (type, resource, params) => {
    let url = '';
    const { queryParameters } = fetchUtils;
    const options = { credentials: 'include' };
    switch (type) {
    case GET_LIST: {
        const { page, perPage } = params.pagination;
        const { field, order } = params.sort;
        const query = {
            offset: (page -1) * perPage
        };
        let entryPoint = resource == 'entry' ? 'entries' : resource + 's';
        url = `${API_URL}/${entryPoint}?${queryParameters(query)}`;
        break;
    }
    case GET_ONE:
        url = `${API_URL}/${resource}/${params.id}`;
        break;
    case GET_MANY: {
        const query = {
            filter: JSON.stringify({ id: params.ids }),
        };
        url = `${API_URL}/${resource}?${queryParameters(query)}`;
        break;
    }
    case GET_MANY_REFERENCE: {
        const { page, perPage } = params.pagination;
        const { field, order } = params.sort;
        const query = {
            sort: JSON.stringify([field, order]),
            range: JSON.stringify([(page - 1) * perPage, (page * perPage) - 1]),
            filter: JSON.stringify({ ...params.filter, [params.target]: params.id }),
        };
        url = `${API_URL}/${resource}?${queryParameters(query)}`;
        break;
    }
    case UPDATE:
        url = `${API_URL}/${resource}/${params.id}`;
        options.method = 'PUT';
        options.body = JSON.stringify(params.data);
        break;
    case CREATE:
        url = `${API_URL}/${resource}`;
        const { fetchJson } = fetchUtils;
        options.method = 'POST';
        if(params.data.files){
          var formData = new FormData()
          formData.append('image', params.data.files[0].rawFile)
          options.body = formData

          return fetchJson(url, { credentials:'include' })
          .then((response, type, resource, params)=>{
            const { headers, json } = response
            url = json.uri;
            return { url, options }
          })
        } else  {
          options.body = JSON.stringify(params.data);
        }
        break;
    case DELETE:
        url = `${API_URL}/${resource}/${params.id}`;
        options.method = 'DELETE';
        break;
    default:
        throw new Error(`Unsupported fetch action type ${type}`);
    }
    return Promise.resolve({ url, options });
};

/**
 * @param {Object} response HTTP response from fetch()
 * @param {String} type One of the constants appearing at the top if this file, e.g. 'UPDATE'
 * @param {String} resource Name of the resource to fetch, e.g. 'posts'
 * @param {Object} params The REST request params, depending on the type
 * @returns {Object} REST response
 */
const convertHTTPResponseToREST = (response, type, resource, params) => {
    const { headers, json } = response;
    switch (type) {
    case GET_LIST:
        let data = json;
        let entryPoint = resource == 'entry' ? 'posts' : resource + 's';
        return {
            data: data[entryPoint],
            total: data.total,
        };
    case CREATE:
        return { data: { ...params.data, id: json.id } };
    default:
        // if ( json.entry ){
        //   // json.entry =
        //   json.entry = markdown.markdown.toHTML(json.entry);
        // }
        return { data: json };
    }
};

/**
 * @param {string} type Request type, e.g GET_LIST
 * @param {string} resource Resource name, e.g. "posts"
 * @param {Object} payload Request parameters. Depends on the request type
 * @returns {Promise} the Promise for a REST response
 */
export default (type, resource, params) => {
    const { fetchJson } = fetchUtils;
    return convertRESTRequestToHTTP(type, resource, params)
    .then(({ url, options })=>{
      return fetchJson(url, options)
      .then(response => convertHTTPResponseToREST(response, type, resource, params))
    })
}