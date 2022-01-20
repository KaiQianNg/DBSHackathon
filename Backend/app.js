const express = require('express');
const dotenv = require('dotenv');
const bodyParser = require('body-parser');
const backend = require('./src/index')
const mysql = require('mysql2');

const app=express();
dotenv.config();
app.use(bodyParser.urlencoded({ extended: true}));

const PORT = 3000;

//change for your own local db
global.pool = mysql.createPool({
    host:'localhost',
    port: '3306',
    database: 'socialmedia',
    user:process.env.DB_USER,
    password:process.env.DB_PASS
});

app.get('/', backend.homepage); //[2] all users post
app.post('/post', backend.post); //[3] insert new post
app.post('/myposts', backend.mypost) //[4] logged in user post
app.post('/update', backend.update); //[5] update post
app.post('/delete', backend.delete); //[6] delete post

app.listen(PORT, ()=>console.log(`Listening to PORT ${PORT}`));