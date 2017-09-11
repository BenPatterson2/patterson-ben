import debounce from 'lodash.debounce';
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Delta from 'quill-delta';

import Quill from 'quill';

require('./RichTextInput.css');

class RichTextInput extends Component {
    componentDidMount() {
        const {
            input: {
                value,
            },
            toolbar,
        } = this.props;

        this.quill = new Quill(this.divRef, {
            modules: { toolbar },
            theme: 'snow',
        });
        const toolbarModule = this.quill.getModule('toolbar');

        function showImageUI() {
          var txt = window.prompt('Enter a src url', '')
          let range = this.quill.getSelection(true);
          this.quill.updateContents(new Delta()
            .retain(range.index)
            .delete(range.length)
            .insert({ image: txt })
          );
        }

        toolbarModule.addHandler('image', showImageUI);
        this.quill.pasteHTML(value);

        this.editor = this.divRef.querySelector('.ql-editor');
        this.quill.on('text-change', debounce(this.onTextChange, 500));



    }

    componentWillUnmount() {
        this.quill.off('text-change', this.onTextChange);
        this.quill = null;
    }

    onTextChange = () => {
        this.props.input.onChange(this.editor.innerHTML);
    }

    updateDivRef = ref => {
        this.divRef = ref;
    }


    render() {
        return <div className='aor-rich-text-input'>
            <div ref={this.updateDivRef} />
        </div>
    }
}

RichTextInput.propTypes = {
    addField: PropTypes.bool.isRequired,
    addLabel: PropTypes.bool.isRequired,
    input: PropTypes.object,
    label: PropTypes.string,
    options: PropTypes.object,
    source: PropTypes.string,
    toolbar: PropTypes.oneOfType([
        PropTypes.array,
        PropTypes.bool,
    ]),
};

RichTextInput.defaultProps = {
    addField: true,
    addLabel: true,
    options: {},
    record: {},
    toolbar: true,
};

export default RichTextInput;