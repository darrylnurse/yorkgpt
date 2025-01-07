export interface Message {
    content: string,
    role: 'user' | 'gpt' | 'system',
}
