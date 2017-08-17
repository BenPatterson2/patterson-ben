import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { jsonServerRestClient, Admin, Resource } from 'admin-on-rest';
import { EntryList, EntryEdit, EntryCreate } from './entries';
import restClient from './restClient';

const App = () => (
    <Admin restClient={restClient}>
        <Resource name="entry" list={EntryList} create={EntryCreate} edit={EntryEdit} />
    </Admin>
);

export default App;
