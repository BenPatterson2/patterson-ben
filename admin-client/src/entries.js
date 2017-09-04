import React from 'react';
import {
    Create,
    Edit,
    BooleanInput,
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
import RichTextInput from 'aor-rich-text-input';
import markdown from 'markdown';
import ChevronLeft from 'material-ui/svg-icons/navigation/chevron-left';
import ChevronRight from 'material-ui/svg-icons/navigation/chevron-right';
import { Toolbar, ToolbarGroup } from 'material-ui/Toolbar';

const cardActionStyle = {
    zIndex: 2,
    display: 'inline-block',
    float: 'right',
};

const PostPagination = ({ page, perPage, total, setPage }) => {
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




const PostEditActions = ({ basePath, data, refresh }) => (
    <CardActions style={cardActionStyle}>
        <ListButton basePath={basePath} />
        <DeleteButton basePath={basePath} record={data} />
    </CardActions>
);



export const EntryList = (props) => (
    <List {...props} pagination={<PostPagination />} >
        <Datagrid>
            <TextField source="created" />
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
            <BooleanInput source="published" />
            <TextInput source="title" />
            <RichTextInput source="entry" validation={{ required:true }}  />
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
            <BooleanInput source="published" />
            <DisabledInput label="Id" source="id" />
            <TextInput source="title" />
            <RichTextInput source="entry" validation={{ required:true }} />
        </SimpleForm>
    </Edit>
);