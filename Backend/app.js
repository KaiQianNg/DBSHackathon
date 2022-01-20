const express = require('express');
const dotenv = require('dotenv');
const bodyParser = require('body-parser');
const backend = require('./src/index')
const mysql = require('mysql2');
const cors = require('cors')

const app=express();
dotenv.config();
app.use(bodyParser.json());
app.use(cors({origin:'*'}))

const PORT = 3002;

//change for your own local db
global.pool = mysql.createPool({
    host:'127.0.0.1',
    port: '3306',
    database: 'socialmedia',
    user:process.env.DB_USER,
    password:process.env.DB_PASS
});

app.get('/', backend.homepage); //[2] all users post
app.post('/post', backend.post); //[3] insert new post
app.post('/myposts', backend.myposts) //[4] logged in user post
app.post('/update', backend.update); //[5] update post
app.post('/delete', backend.delete); //[6] delete post

app.listen(PORT, ()=>console.log(`Listening to PORT ${PORT}`));