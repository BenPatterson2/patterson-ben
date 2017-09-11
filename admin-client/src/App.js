import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { jsonServerRestClient, Admin, Resource } from 'admin-on-rest';
import { EntryList, EntryEdit, EntryCreate, EntryDelete } from './entries';
import { ImageList, ImageEdit, ImageCreate, ImageDelete } from './images';
import restClient from './restClient';


const App = () => (
    <Admin restClient={restClient}>
        <Resource
          name="entry"
          list={EntryList}
          create={EntryCreate}
          edit={EntryEdit}
          remove={EntryDelete} />
          <Resource
            name="image"
            list={ImageList}
            create={ImageCreate}
            edit={ImageEdit}
            remove={ImageDelete} />
    </Admin>
);

export default App;
