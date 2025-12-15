'use client'
import { useState } from 'react'


export default function Login(){
const [user,setUser]=useState('')
const [pass,setPass]=useState('')


async function submit(e){
e.preventDefault()
const res = await fetch('http://localhost:8000/auth/login', {
method:'POST', headers:{'Content-Type':'application/json'},
body: JSON.stringify({username:user,password:pass})
})
const data = await res.json()
if (data.access_token) {
localStorage.setItem('token', data.access_token)
window.location.href='/'
}
}


return (
<div className="max-w-md mx-auto p-6 bg-gray-800 rounded">
<h2 className="text-2xl font-bold mb-4">Вход</h2>
<form onSubmit={submit} className="flex flex-col gap-3">
<input className="p-2 bg-gray-700 rounded" placeholder="username" value={user} onChange={e=>setUser(e.target.value)} />
<input className="p-2 bg-gray-700 rounded" placeholder="password" type="password" value={pass} onChange={e=>setPass(e.target.value)} />
<button className="bg-yellow-400 text-black p-2 rounded">Войти</button>
</form>
</div>
)
}