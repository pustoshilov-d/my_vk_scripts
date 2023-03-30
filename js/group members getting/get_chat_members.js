const api = require('vk-easy');
api('messages.getConversationMembers', {
    group_id: 23513715,
    peer_id:2000000001,
    access_token: '',
    v: "5.131"
}).then((res, err)  => {
    if (err) {
        console.log(err)
    } else {
        console.log(res)
        console.log(Object.keys(res.response))
        // console.log(Object.keys(res.response.profiles))
        var mass=res.response.items
        for (var item in mass) {
            console.log(mass[item].member_id)
        }
        // console.log(res.response.items.toString());
    }
});
