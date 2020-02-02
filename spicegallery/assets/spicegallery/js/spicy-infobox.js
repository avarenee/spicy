const div = (className, content = "", style = "") => {
  var fragment = document.createElement('div');
  fragment.classList.add(className);
  fragment.innerHTML = content;
  fragment.setAttribute("style", style);
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

class SpicyInfo extends HTMLElement {
  constructor() {
    super();
    var spice = this.getAttribute('spice_name');
    var color = this.getAttribute('color');
    var image = `static/spicegallery/images/${spice.replace(/\s/g, '')}.jpg`
    var basic = this.getAttribute('basic');
    var extended = this.getAttribute('extended');

    var spicyinfobox =
      template(
        [ this,
          [ div("card"),
            [ div("header", spice.toUpperCase(), `background-color:${color};`),
              div("card-inner"),
              [ div("basic"),
                [ div("text", basic), div("image", `<img src=${image}>`) ],
                div("extended", extended)
              ],
              div("footer")
            ]
          ]
        ]
      );
  }
}

customElements.define('spicy-infobox', SpicyInfo);
