export default function ChatBubble ({text, role}) { // t/i here

    let alignValue : string = '';
    let colorValue : string = '';
    if (role === 'user') {
        alignValue = 'end';
        colorValue = 'lightblue';
    } else if (role === 'gpt') {
        alignValue = 'start';
        colorValue = 'lightgreen';
    } else {
        alignValue = 'center';
        colorValue = 'orange';
    }

    return (
        <li className={'chat-row'}>
            <div
                className={'bubble'}
                style={{
                    alignSelf: alignValue,
                    backgroundColor: colorValue,
                }}
            >
                {text}
            </div>
        </li>
    )
}