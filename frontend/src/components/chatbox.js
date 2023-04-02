import {useState} from 'react';
import React, { useRef, useEffect } from 'react';
import MsgEntry from './msg_entry'
import Prompt from './prompt';
import Response from './response';

function ChatBox (){


    let messageComponent = []; //A message component includes a message and its respons.
    const [messagesArray, setMessagesArray] = useState([]);
    const ai = 'I am your AI';
    
    if(messagesArray.length > 0){
        console.log(messagesArray)
        messageComponent = messagesArray.map((message, i)=>{
        return(
            <div>
                <Prompt key={"prompt-" + i}text={message}/> 
                <Response key={"response-" + i} text={ai}/>
            </div>
        );
        })
    }


    window.scrollTo(0, document.body.scrollHeight);
    return(
        <div className="bg-[#2f4454] flex w-full h-full flex-col" >         
            <div>{messageComponent}</div>
            <br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
            <MsgEntry setMessagesArray={setMessagesArray} messagesArray={messagesArray} />
         
        </div>
    );

    
}

export default ChatBox;