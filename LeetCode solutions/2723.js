type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    const result = await Promise.all([promise1, promise2]);
    
    // Calculate the sum of the resolved values
    const sum = result.reduce((acc, curr) => acc + curr, 0);
    
    // Resolve the new promise with the sum
    return Promise.resolve(sum);
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */