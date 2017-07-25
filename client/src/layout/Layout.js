import React from "react";

import NavbarInstance from "../components/layout/NavbarInstance";

export default class Layout extends React.Component {
  render() {
    return (
      <div>
        <NavbarInstance />
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              {this.props.children}
            </div>
          </div>
        </div>
      </div>
    );
  }
}
