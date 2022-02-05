import React, { Component } from "react";
import axios from "axios"



function getToken() {
  const tokenString = sessionStorage.getItem('token');
  const userToken = JSON.parse(tokenString);
  return userToken['access']
}

async function getPokemon() {
    const url = 'http://127.0.0.1:8000/game/pokemon/kanto'
    return fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + getToken()
      }
    })
    .then(result => {
      if(!result.ok)
        throw new Error(result.status);
      else {
        return result.data
      }
      
    })
  }
    

class Pokemon extends Component{
  listitems = getPokemon()
  pokelist = []




  getList = () => {
    console.log(getPokemon())
  }
  

  render() {

    return (
      <React.Fragment>
        <ul class='list-group'>
          {this.pokelist.map(item =>(
            <li key={item.id}>
            {item.name}
          </li>
          ))}
        </ul>
        <button onClick={this.getList}>get list</button>
      </React.Fragment>
    )
  }
}

export default Pokemon
  
  

