import React from 'react';
import { Link } from 'react-router-dom';

const MyPostCard = (props) => {
    const  post  = props.post;

    return(
        <div>
            <div>
                <h3>{post.Post_Title}</h3>
            </div>
        </div>
    )
};

export default MyPostCard;