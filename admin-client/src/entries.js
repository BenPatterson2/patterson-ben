import React from 'react';
import { List, Datagrid, TextField } from 'admin-on-rest';

export const EntryList = (props) => (
    <List {...props}>
        <Datagrid>
            <TextField source="id" />
            <TextField source="title" />
            <TextField source="entry" />
        </Datagrid>
    </List>
);