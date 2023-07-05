/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        const timeoutPromise = new Promise((_,reject)=>{
            setTimeout(()=>{
                reject('Time Limit Exceeded')
            },t)
        })
        return Promise.race([fn(...args),timeoutPromise])
    }
};

/**
    Promise.race([fn(...args),timeoutPromise])
    which returns first
    As fn(...args) will get executed normally but timeoutPromise will be wasting its 
    time,if fn(...args) get executed first our result will what it returns,else a reject 
    promise 

 */

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
