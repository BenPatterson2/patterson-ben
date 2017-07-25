import React from "react";

export default class Layout extends React.Component {
  render() {
    return (
      <div>
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
