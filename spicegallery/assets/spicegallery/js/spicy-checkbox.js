var svg_checkmark = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path d="M9 21.035l-9-8.638 2.791-2.87 6.156 5.874 12.21-12.436 2.843 2.817z"/></svg>`;

const checkbox = (attributes) => {
  var fragment = document.createElement('input');
  for (const attribute in attributes) {
    fragment.setAttribute(attribute, attributes[attribute]);
  }
  return fragment
}

const span = (className, content = "") => {
  var fragment = document.createElement('span');
  fragment.classList.add(className);
  fragment.innerHTML = content;
  return fragment
}

const label = (attributes, content = "") => {
  var fragment = document.createElement('label');
  for (const attribute in attributes) {
    fragment.setAttribute(attribute, attributes[attribute]);
  }
  fragment.innerHTML = content;
  return fragment
}

function template(elements) {
  var root = elements[0];
  var children = elements[1];
  children.forEach((child, index) => {
    if (Array.isArray(child)) {
      return template([children[index - 1], child]);
    } else {
      root.appendChild(child);
    }
  });
  return root
}

class SpicyCheck extends HTMLElement {
  constructor() {
    super();
    var spice = this.getAttribute('spice_name');
    var spice_id = this.getAttribute('spice_id');

    var inputAttributes = {
      'type': 'checkbox',
      'spice_id': spice_id,
      'id': 'spice' + spice_id,
      'name': 'spice',
      'value': spice
    }

    var labelAttributes = {
      'for': 'spice' + spice_id
    }

    var spicycheckbox =
      template(
        [ this,
          [ checkbox(inputAttributes),
            span("customcheck", svg_checkmark),
            label(labelAttributes, spice)
          ]
        ]
      );
  }
}

customElements.define('spicy-checkbox', SpicyCheck);
