const { log } = require("console");
const { PythonShell } = require("python-shell");
const express = require("express");

const app = express();
app.use(express.urlencoded({ extended: false }))
app.use(express.static("static"))


const con = async (from, to,between, blocks) => {
    let options = {
        mode: "text",
        pythonOptions: ['-u'],
        args : [JSON.stringify(from),JSON.stringify(to),JSON.stringify(between),blocks]
    }
    return PythonShell.run("Python/backend.py", options)
}
let r = {"status":false}
app.get("/blocks", (req, res) => {
    let { data } = req.query
    let { from_color, to_color,between_color, blockNo } = JSON.parse(req.query.data)
    try {
        con(from_color, to_color,between_color, blockNo).then((msg, err) => {
            if(err)
                throw err;
            else {
                r["status"] = true
                r["blocks"] = msg
                res.status(200).json(r)
            }
        })
    }
    catch {
        res.status(404).json(r)
    }
})
app.listen(5000, () => {
    log("server running at port 5000")
})