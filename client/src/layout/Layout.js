import React from "react";

import NavbarInstance from "../components/layout/NavbarInstance";

export default class Layout extends React.Component {
  render() {
    return (
      <div>
        <NavbarInstance />
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              {this.props.children}
            </div>
          </div>
        </div>
      </div>
    );
  }
}
