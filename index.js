const { log } = require("console");
const { PythonShell } = require("python-shell");
const express = require("express");

const app = express();
app.use(express.urlencoded({ extended: false }))
app.use(express.static("static"))

options = {
    mode: "text",
    pythonOptions: ['-u'],
    args : []
}
const con = async () => {
    PythonShell.run("Python/backend.py", options).then((msg,err) => {
        if (err)
            throw err;
        log(msg)

    })
}
con()

app.get("/", (req, res) => {
    res.end()
})
app.listen(5000, () => {
    log("server running at port 5000")
})