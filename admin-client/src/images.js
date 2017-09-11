import React from 'react';
import {
    Create,
    Edit,
    BooleanInput,
    SimpleForm,
    DisabledInput,
    DateInput,
    List,
    ListButton,
    LongTextInput,
    ReferenceManyField,
    Datagrid,
    TextField,
    TextInput,
    FileInput,
    FileField,
    ImageField,
    DateField,
    Delete,
    DeleteButton,
    EditButton
  } from 'admin-on-rest';
import { CardActions } from 'material-ui/Card';
import FlatButton from 'material-ui/FlatButton';
import NavigationRefresh from 'material-ui/svg-icons/navigation/refresh';
import ChevronLeft from 'material-ui/svg-icons/navigation/chevron-left';
import ChevronRight from 'material-ui/svg-icons/navigation/chevron-right';
import { Toolbar, ToolbarGroup } from 'material-ui/Toolbar';

const cardActionStyle = {
    zIndex: 2,
    display: 'inline-block',
    float: 'right',
};

const ImagePagination = ({ page, perPage, total, setPage }) => {
    const nbPages = Math.ceil(total / perPage) || 1;
    return (
        nbPages > 1 &&
            <Toolbar>
                <ToolbarGroup>
                {page > 1 &&
                    <FlatButton primary key="prev" label="Prev" icon={<ChevronLeft />} onClick={() => setPage(page - 1)} />
                }
                {page !== nbPages &&
                    <FlatButton primary key="next" label="Next" icon={<ChevronRight />} onClick={() => setPage(page + 1)} labelPosition="before" />
                }
                </ToolbarGroup>
            </Toolbar>
    );
}




const ImageEditActions = ({ basePath, data, refresh }) => (
    <CardActions style={cardActionStyle}>
        <ListButton basePath={basePath} />
        <DeleteButton basePath={basePath} record={data} />
    </CardActions>
);



export const ImageList = (props) => (
    <List {...props} pagination={<ImagePagination />} >
        <Datagrid>
            <TextField source="id" />
            <ImageField source="servingUri" />
            <EditButton />
        </Datagrid>
    </List>
);



export const ImageCreate = (props) => (
    <Create {...props}>
        <SimpleForm>
            <FileInput title="image" source="files" label="Related files" accept="image/*">
              <FileField source="src" title="title" />
           </FileInput>
        </SimpleForm>
    </Create>
);

export const ImageDelete = (props) => (
    <Delete {...props}>

    </Delete>
);


const required = { required:true };

export const ImageEdit = (props) => (

    <Edit {...props} actions={<ImageEditActions />}>
        <SimpleForm>
            <TextField source="id" />
            <TextInput source="servingUri" />
            <ImageField source="servingUri" />
        </SimpleForm>
    </Edit>
);