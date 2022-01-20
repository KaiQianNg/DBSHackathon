import React from 'react';
import { Link } from 'react-router-dom';

const MyPostCard = (props) => {
    const  post  = props.post;

    return(
        <div>
            <div>
                <img src={post.Post_Image} ></img>
                <h3>{post.Post_Title}</h3>
                <p>{post.Post_Description}</p>
            </div>
        </div>
    )
};

export default MyPostCard;