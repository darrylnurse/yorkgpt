export default function LoadingBubble () {
    return (
        <li className={'chat-row'}>
            <div className={'bubble loading-bubble'}>
                <div style={{
                    animationDelay: '0s'
                }}>.</div>
                <div style={{
                    animationDelay: '0.5s'
                }}>.</div>
                <div style={{
                    animationDelay: '1s'
                }}>.</div>
            </div>
        </li>
    )
}