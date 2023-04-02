import {useState, useRef} from 'react';
import Prompt from './prompt';
import Response from './response';
import { BsFillSendFill } from 'react-icons/bs';


const MsgEntry = (props) => {
     
    // const [prompt, setPrompt] = useState(null);
    const textRef = useRef();

    const getAPIResponse = async (prompt) => {  
        console.log('Waiting for the server to respond')
        try {
          const apiUrl = 'http://3.209.61.33/';
          const queryParams = new URLSearchParams({query: prompt});
          const url = apiUrl + '?' + queryParams;
          const response = await fetch(url);
          const jsonData = await response.json();
          console.log(jsonData);
          return jsonData;
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      }
      

    const sendMessage = async (e) => {
        const newMessage = textRef.current.value
        console.log('message: ' + newMessage);
        var gpt_reply = await getAPIResponse(newMessage);
        // var gpt_reply = "I'm your reply";
        var messageComp = {'user_message': newMessage, "gpt_reply": gpt_reply.reply}
        const updatedMessagesArray = [...props.messagesArray, messageComp];
        // get the response from API
        props.setMessagesArray(updatedMessagesArray);
        textRef.current.value = '';
    }

    return(
        <div className="bg-[#3c586e] w-100 h-20 flex m-12 fixed bottom-0 rounded-xl p-1 shadow-md shadow-black" >
            
            <textarea className="bg-[#3c586e] focus:outline-none text-white resize-none" 
                ref={textRef}
                placeholder="Enter your message here..." name="" id="message" cols="110" rows="10"
                onKeyDown={(event) => {
                    if (event.keyCode === 13) {
                        sendMessage();
                    }
                }}>
            </textarea>
            <button onClick={sendMessage}>
                <BsFillSendFill className ='m-2 text-white'/>
            </button>
        </div>
    );
}

export default MsgEntry;