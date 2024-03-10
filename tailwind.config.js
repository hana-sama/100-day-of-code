/** @type {import('tailwindcss').config} */
module.exports = {
    mode: "jit",
    content: [
        "./templates/**/*.html",
        "./static/**/*.js",
        "./node_modules/flowbite/**/*.js"
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require("flowbite/plugin")
    ],
}
