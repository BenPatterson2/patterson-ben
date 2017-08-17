import debounce from 'lodash.debounce';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import TextField from 'material-ui/TextField';
import { FieldTitle }from 'admin-on-rest';
import { markdown } from 'markdown';


require('./MarkdownInput.css');


export class MarkdownInput extends Component {
  constructor() {
      super();
      this.state = {
        preview:  { __html: markdown.toHTML('') }

      };
    }

    handleBlur = (eventOrValue) => {
        this.props.onBlur(eventOrValue);
        this.props.input.onBlur(eventOrValue);
    }

    handleFocus = (event) => {
        this.props.onFocus(event);
        this.props.input.onFocus(event);
    }

    handleChange = (eventOrValue) => {
        this.props.onChange(eventOrValue);
        this.props.input.onChange(eventOrValue);
        debounce(this.onTextChange, 500);
        this.onTextChange()
    }

     onTextChange = () =>{

       this.setState({
         preview:{ __html: markdown.toHTML(this.props.input.value)}
       })
     }

    render() {
      var divStyle = {
            color: 'red',
            'background-color':'red'
          };

        const {
            elStyle,
            input,
            isRequired,
            label,
            meta: { touched, error },
            options,
            resource,
            source,
            type,
        } = this.props;
        return (
            <div >
               <TextField
                {...input}
                multiLine
                fullWidth
                onBlur={this.handleBlur}
                onFocus={this.handleFocus}
                onChange={this.handleChange}
                type={type}
                floatingLabelText={
                  <FieldTitle label={label}
                     source={source}
                     resource={resource}
                     type='text'
                     isRequired={isRequired}
                  />}
                errorText={touched && error}
                style={elStyle}
                {...options}
               />
             <div className='markdown-container'>
               <div dangerouslySetInnerHTML= { this.state.preview } ></div>
             </div>
           </div>
        );
    }
}

MarkdownInput.propTypes = {
    addField: PropTypes.bool.isRequired,
    elStyle: PropTypes.object,
    input: PropTypes.object,
    isRequired: PropTypes.bool,
    label: PropTypes.string,
    meta: PropTypes.object,
    name: PropTypes.string,
    onBlur: PropTypes.func,
    onChange: PropTypes.func,
    onFocus: PropTypes.func,
    options: PropTypes.object,
    resource: PropTypes.string,
    source: PropTypes.string,
    type: PropTypes.string,
};

MarkdownInput.defaultProps = {
    addField: true,
    onBlur: () => {},
    onChange: () => {},
    onFocus: () => {},
    options: {},
    type: 'textarea',
};

export default MarkdownInput;