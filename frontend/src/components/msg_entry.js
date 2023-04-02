import {useState, useRef} from 'react';
import Prompt from './prompt';
import Response from './response';
import { BsFillSendFill } from 'react-icons/bs';


const MsgEntry = (props) => {
     
    // const [prompt, setPrompt] = useState(null);
    const textRef = useRef();

    const getAPIResponse = async (prompt) => {
        try {
          console.log('waiting for the server to respond')
          const queryParams = new URLSearchParams({query: prompt})
          const response = await fetch("http://127.0.0.1:8000?" + queryParams);
          const jsonData = await response.json();
          console.log(jsonData);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      }
      

    const sendMessage = async (e) => {
        const newMessage = textRef.current.value
        console.log('message: ' + newMessage);
        const updatedMessagesArray = [...props.messagesArray, newMessage];
        // get the response from API
        props.setMessagesArray(updatedMessagesArray);
        textRef.current.value = '';
        getAPIResponse(newMessage);
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