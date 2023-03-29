import React , {useState, useEffect}from "react"
import "./MainSection.css"


function MainSection(props){
    
    const [status, setStatus] = React.useState(true);

    const [state, setState] = React.useState({
        num1: Math.floor((Math.random() * 10)),
        num2: Math.floor((Math.random() * 10)),
        score: 0,
        response: "",
        incorrect : false
    });

    function updateResponse(event){
        setState({
            ...state,
            response : event.target.value
        })
    }

    function checkresponse(event){
        if (event.key === "Enter"){
            if(parseInt(state.response) === state.num1 + state.num2){
                setState({
                    ...state,
                    score:  state.score + 1,
                    response: "",
                    num1: Math.floor((Math.random() * 10)),
                    num2: Math.floor((Math.random() * 10)),
                    incorrect : false
                }) 
            } else {
                setState({
                    ...state,
                    incorrect : true,
                    score: state.score-1,
                    response: ""
                    
                })
            }
        }
    }

    if(state.score > 5){
        return(
            <section className="main">
                <h1>You win</h1>
            </section>
        )
    }
    if(state.score < -5){
        return(
            <section className="main">
                <h1>You lose</h1>
            </section>
        )
    }

    return(
        <section className="main">
            
            <h1 className={state.incorrect ? "incorrect" : ""}>{state.num1} + {state.num2} = ?</h1>
            <br></br>
            <input type="text" value={state.response} placeholder="Put your answer here" onChange={updateResponse} onKeyPress={checkresponse} />
            <br></br>
            <p>Your score is : {state.score}</p>
    
        </section>

    )
}

export default MainSection;