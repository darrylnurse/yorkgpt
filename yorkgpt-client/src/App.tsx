import {ReactElement, useEffect, useRef, useState} from "react";
import ChatBubble from "./components/ChatBubble.tsx";
import {
    Message
} from 'types/ConversationTypes.ts'
import LoadingBubble from "./components/LoadingBubble.tsx";

function App() {

    const [conversation, setConversation] = useState<Message[]>([
        {content: 'Hi', role: 'user'},
        {content: 'hellooo', role: 'gpt'}
    ]);
    const [query, setQuery] = useState<Message>({
        content: '',
        role: 'user'
    });

    const handleQueryChange = (event) => {
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        const { _, value} = event.target;

        setQuery((prev): Message => ({
            ...prev,
            content: value
        }))
    }

    const [queryComplete, setQueryComplete] = useState(true);
    const queryModel = async () => {
        setQueryComplete(false);

        const requestUrl : string = 'http://192.168.1.2:3000/yorkgpt';
        const queryConfig: RequestInit = {
            method: 'POST',
            headers:  {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                question: query.content
            })
        }

        try {
            const response = await fetch(requestUrl, queryConfig);
            const reply = await response.json();
            setConversation(prevConversation => [...prevConversation, { content: reply.result, role: 'gpt' }]);
            setQueryComplete(true);
        } catch(error) {
            setQueryComplete(true);
            setConversation(prevConversation => [...prevConversation, { content: 'Server query failed. Try again when the service is available.', role: 'system' }]);
            console.error(error.message);
        }
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        if(!query.content) {
            alert('Must enter query.');
            return;
        }

        setConversation(prevConversation => [...prevConversation, query]);
        setQuery({
            content: '',
            role: 'user'
        })

        queryModel().catch(console.error);
    }

    const messageRef = useRef(null);

    useEffect(() => {
        if(messageRef.current) {
            messageRef.current.scrollIntoView({ behavior: 'smooth'});
        }
    }, [conversation])

  return (
      <section className={'chat-page'}>
          <header className={'chat-header'}>
            YorkGpt
          </header>
          <main className={'chat-main'}>
              <ul
                  className={'conversation'}
              >
                  { conversation &&
                      conversation.map((message, messageIndex) : ReactElement => (
                          <ChatBubble
                              text={message.content}
                              role={message.role}
                              key={messageIndex}
                          />
                      ))
                  }
                  {!queryComplete && <LoadingBubble/>}
                  <div ref={messageRef}>
                  </div>
              </ul>
          </main>
          <footer className={'chat-footer'}>
              <form
                  className={'user-input'}
                  onSubmit={handleSubmit}
              >
                  <input
                    type={'text'}
                    className={'user-query'}
                    onChange={handleQueryChange}
                    value={query.content}
                  />
                  <button
                    className={'query-submit'}
                    type={queryComplete ? 'submit' : 'button'}
                    style={{
                        opacity: queryComplete ? 1 : 0.5,
                    }}
                  >
                      Submit
                  </button>
              </form>
          </footer>
      </section>
  )
}

export default App
