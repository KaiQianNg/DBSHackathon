export const req = async(url, data)=>{
    try{
        return await fetch(`http://localhost:3002/${url}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
    } catch (err) {
        console.log(err);
    }
}