import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {Col, Row} from "react-bootstrap"

import axios from "axios";
import MyPostCard from "./MyPostCard";

const UserProfile = () => {

    const [myposts, setPosts] = useState([]);

    useEffect(() => {
        axios
        .get('http://localhost:3002/')
        .then(res => {
            setPosts(res.data)
        })
        .catch(err => {
            console.log(err);
        })
    })

    console.log(myposts)

    let postList;

    if(!myposts) {
        postList = "there is no post record!";
    } else {
        postList = myposts.map((post, k) =>
        <MyPostCard post={post} key={k} />
        );
    }

    return(
        <>
            <Row>
                <h4>Name</h4>
                {postList}
            </Row>
        </>
    )

}

export default UserProfile;