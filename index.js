const { log } = require("console");
const { PythonShell } = require("python-shell");
const express = require("express");

const app = express();
app.use(express.urlencoded({ extended: false }))
app.use(express.static("static"))


const con = async (from, to, blocks) => {
    let options = {
        mode: "text",
        pythonOptions: ['-u'],
        args : [JSON.stringify(from),JSON.stringify(to),blocks]
    }
    return PythonShell.run("Python/backend.py", options)
}
app.get("/blocks", (req, res) => {
    let { data } = req.query
    let { from_color, to_color, blockNo } = JSON.parse(req.query.data)
    con(from_color, to_color, blockNo).then((msg, err) => {
        if(err)
            throw err;
        else
            log(msg)
    })
    res.status(200).json({"status":true,"data":data})
})
app.listen(5000, () => {
    log("server running at port 5000")
})