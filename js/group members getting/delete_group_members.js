const api = require('vk-easy');

// TOKEN from https://oauth.vk.com/authorize?client_id=7432908&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=groups&response_type=token&v=5.131&state=123456
// or GROUP_TOKEN
const TOKEN = ""
const str = "4115685,4316480"
// const str = "360794785"

const timer = ms => new Promise(res => setTimeout(res, ms))

async function load() { // We need to wrap the loop into an async function for this to work
  const users = str.split(",")
  console.log(users.length)

  for (const user of users) {
    console.log(user)
    api('groups.removeUser', {
      group_id: 210258394,
      user_id: user,
      access_token: TOKEN,
      v: "5.131"
    }).then((res, err) => {
      console.log('object :>> ', res, err)
    })
    await timer(1000)
  }
}

load();
