//authentication not done

exports.homepage = async (req, res) => {
    const client = global.pool;
    try {
        var query = `SELECT * FROM post`;
        const result = await client.promise().query(query);
        const results = {results:result[0]}
        res.send(results)
    } catch (err) {
        console.log(err);
    }
}

exports.post = async (req, res) => {
    const client = global.pool;
    //make post req to update post table
}

exports.mypost = async (req, res) => {
    //use req.body.username to filter posts
    const client = global.pool
}

 exports.update = async (req, res) => {
     //use req.body to specify what to update
 }

 exports.delete = async (req, res) => {
     //use req.body to specify what post to delete
 }