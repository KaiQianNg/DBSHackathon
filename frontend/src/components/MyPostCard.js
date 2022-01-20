import React from 'react';
import { Link } from 'react-router-dom';

const MyPostCard = (props) => {
    const  post  = props.post;

    return(
        <div>
            <div style={{borderStyle:'solid', width:'50%', textAlign:'center'}}>
                <img src={post.Post_image} alt="post Title" style={{width:'50%'}}/>
                <h3>{post.Post_Title}</h3>
                <p>{post.Post_Description}</p>
            </div>
        </div>
    )
};

export default MyPostCard;