//authentication not done

exports.homepage = async (req, res) => {
    const client = global.pool;
    try {
        var query = `SELECT * FROM post`;
        const result = await client.promise().query(query);
        const results = { results: result[0] }
        res.send(results)
    } catch (err) {
        console.log(err);
    }
}

exports.post = async (req, res) => {
    const client = global.pool;
    //make post req to update post table
    try {
        var userid = req.body.userid;
        var title = req.body.title;
        var description = req.body.description;
        var image = req.body.image;

        var query = `INSERT INTO post (Post_Title, User_ID, Post_Description, Post_image) values ('${title}', '${userid}', '${description}', '${image}')`
        const result = await client.promise().query(query);
        res.send(result)
    } catch (err) {
        console.log(err);
    }
}

exports.mypost = async (req, res) => {
    //use req.body.username to filter posts
    const client = global.pool
    console.log(req);
    try {
        var userid = req.body.userid;

        var query = `SELECT * from post WHERE User_ID=${userid}`
        const result = await client.promise().query(query);
        const results = { results: result[0] }
        res.send(results)
    } catch (err) {
        console.log(err);
    }
}

exports.update = async (req, res) => {
    //use req.body to specify what to update
    const client = global.pool
    try {
        var postid = req.body.postid
        
        var query = `SELECT * from post WHERE Post_ID=${postid}`
        const result = await client.promise().query(query);
        const retrieved_post = result[0][0]
        if(!retrieved_post){
            res.send(false)
            return;
        }

        var userid = req.body.userid
        var title = req.body.title? req.body.title: retrieved_post.Post_Title
        var description = req.body.description? req.body.description: retrieved_post.Post_Description
        var image = req.body.image? req.body.image: retrieved_post.Post_image

        var check
        if (userid===retrieved_post.User_ID){
            var query = `UPDATE post SET Post_Title='${title}', Post_Description='${description}', Post_image='${image}' WHERE Post_ID=${postid}`
            const update = await client.promise().query(query);
            check = update[0].affectedRows==1;
        } else {
            check = false;
        }
        res.send(check)

    } catch (err) {
        console.log(err);
    }
}

exports.delete = async (req, res) => {
    //use req.body to specify what post to delete
    const client = global.pool
    try {
        var postid = req.body.postid
        var userid = req.body.userid

        var query = `SELECT * from post WHERE Post_ID=${postid}`
        const result = await client.promise().query(query);
        const retrieved_post = result[0][0]
        if(!retrieved_post){
            res.send(false)
            return;
        }
        
        var check;
        if(userid==retrieved_post.User_ID) {
            var query = `DELETE FROM liked_post WHERE Post_ID=${postid}`
            var update = await client.promise().query(query);
            var query = `DELETE FROM post_comment WHERE Post_ID=${postid}`
            update = await client.promise().query(query);
            var query = `DELETE FROM post WHERE Post_ID=${postid}`
            update = await client.promise().query(query);
            check = update[0].affectedRows==1;
        } else {
            check = false;
        }

        res.send(check);

    } catch (err) {
        console.log(err)
    }
}