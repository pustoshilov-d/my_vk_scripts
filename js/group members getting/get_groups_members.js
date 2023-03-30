
const api = require('vk-easy');
api('groups.getMembers', {
    group_id: 23513715,
    sort:"time_desc",
    access_token: '',
    v: "5.131"
}).then((res, err)  => {
    console.log(res.response.items.toString());

});
