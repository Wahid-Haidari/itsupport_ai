import {useState} from 'react';
import MsgEntry from './msg_entry'
import Prompt from './prompt';
import Response from './response';

function ChatBox (){

    //const [prompt, setPrompt] = useState(null);
    let messageComponent = [];
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

    return(
        <div className="bg-[#2f4454] flex w-full h-full flex-col" >         
            <div>{messageComponent}</div>
            <MsgEntry setMessagesArray={setMessagesArray} messagesArray={messagesArray} />
         
        </div>
    );
}

export default ChatBox;