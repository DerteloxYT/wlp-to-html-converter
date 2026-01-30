# 🌐 WLP to HTML Converter 🚀

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python 3 script that converts **WLP (Web Language Program)** files into fully functional HTML pages. It supports `textbox`, `inputtext`, and `button` elements, including `onclick` JavaScript events, and handles head properties like `title`, `wlp-pro-key`, `background-color`, and `text-color`. The output is clean HTML ready to open in any browser. Perfect for developers, hobbyists, or anyone experimenting with WLP pages. ⚡

## 💾 Installation

1. Ensure **Python 3** is installed.  
2. Clone this repository or download the files:

```bash
git clone https://github.com/YourUsername/wlp-html-converter.git
cd wlp-html-converter
```
## You should have:

wlp_converter.py
README.md
No additional libraries are required. ✔️

##💡 Usage
Place your WLP file in the project folder (e.g., example.wlp) and run:
```bash
python wlp_converter.py example.wlp
```
The script will generate output.html in the same folder. Open output.html in your browser to see your page. 🎉

The converter interprets WLP syntax, generates HTML elements, applies styles, and preserves onclick events. All elements like textbox, inputtext, and button will work as expected.

##📝 Example WLP
```bash
start-web-page;
page {
  head {
    title="Example Page";
    wlp-pro-key="WLP-demo";
    style {
      background-color="#303030";
      text-color="white";
    }
  }
  appearance {
    textbox(text="Hello World", onclick="alert('Hello!')");
    inputtext(text="Type something here");
    button(text="Click Me", onclick="alert('Clicked!')");
    textbox(text="Another label example", onclick="console.log('Clicked label')");
    inputtext(text="Another input field");
    button(text="Submit", onclick="alert('Form submitted')");
  }
}
code-end;
```
This example generates an HTML page with 🌟 dark background, white text 🌑, multiple labels with clickable JS events ✨, input fields 🖊️, and buttons that trigger alerts or JS functions ✅.

##⚠️ Notes
Ensure WLP syntax is correct. Invalid syntax may cause errors.

onclick events must contain valid JavaScript.

Currently supports textbox, inputtext, and button.

CSS styles in WLP automatically apply to HTML.

Compatible with modern browsers: Chrome, Firefox, Edge, Safari.

##🎨 Advanced Usage
You can create complex pages with multiple elements, grouped logically, with styles and JS events. Large WLP files are supported. The converter outputs fully self-contained HTML. Ideal for prototyping WLP projects or learning WLP web design. 🚀
```
##📜 License
This project is licensed under the MIT License 🛡️.
Enjoy converting your WLP files to HTML! 🎉💻
