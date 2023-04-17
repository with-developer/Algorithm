function solution(s) {
    var answer = -1;
    let filtering = true
    const stack = [];

    for( let i of s ){
        stack.push(i)
        if(stack[stack.length-1] == stack[stack.length-2] ){
            stack.pop()
            stack.pop()
        }
    } 
    answer = stack.length == 0 ? 1 : 0;
    return answer;
}
