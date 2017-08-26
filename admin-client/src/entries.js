import React from 'react';
import {
    Create,
    Edit,
    SimpleForm,
    DisabledInput,
    TextInput,
    DateInput,
    List,
    ListButton,
    LongTextInput,
    ReferenceManyField,
    Datagrid,
    TextField,
    DateField,
    Delete,
    DeleteButton,
    EditButton
  } from 'admin-on-rest';
import { CardActions } from 'material-ui/Card';
import FlatButton from 'material-ui/FlatButton';
import NavigationRefresh from 'material-ui/svg-icons/navigation/refresh';
import MarkdownInput from './aor-markdown-input/src/index';

const cardActionStyle = {
    zIndex: 2,
    display: 'inline-block',
    float: 'right',
};

const PostEditActions = ({ basePath, data, refresh }) => (
    <CardActions style={cardActionStyle}>
        <ListButton basePath={basePath} />
        <DeleteButton basePath={basePath} record={data} />
    </CardActions>
);



export const EntryList = (props) => (
    <List {...props}>
        <Datagrid>
            <TextField source="id" />
            <TextField source="title" />
            <TextField source="entry" />
            <EditButton />
        </Datagrid>
    </List>
);



export const EntryCreate = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="title" />
            <MarkdownInput source="entry" elStyle={{
                'verticalAlign':'top',
                 height: '300px',
                 width:'400px',
              }} />
        </SimpleForm>
    </Create>
);

export const EntryDelete = (props) => (
    <Delete {...props}>

    </Delete>
);


const required = { required:true };

export const EntryEdit = (props) => (
    <Edit {...props} actions={<PostEditActions />}>
        <SimpleForm>
            <DisabledInput label="Id" source="id" />
            <TextInput source="title" />
            <MarkdownInput source="entry" elStyle={{
                'verticalAlign':'top',
                 height: '300px',
                 width:'400px',
              }} />
        </SimpleForm>
    </Edit>
);