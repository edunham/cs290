function actual_compare(a,b){
    // According to
    // http://stackoverflow.com/questions/1068834/object-comparison-in-javascript
    // this will work in the real world. So much less icky and verbose.
    return Object.toJSON(a) == Object.toJSON(b)
}

function recursive_compare(a,b){
    for (var item in a){
        if (a.hasOwnProperty(item)){
            if (!b.hasOwnProperty(item)){
                // picked up hasOwnProperty from an answer in
                // http://stackoverflow.com/questions/201183/how-to-determine-equality-for-two-javascript-objects/16788517
                return false;
            }// a contained something that wasn't in b
            if (!educational_compare(a[item], b[item])){
                return false;
            }
            return true;
        }
        if (a[item] === b[item]){
            return true;
        } // supposing this hasOwnProperty might not always work
        return false;
    }
}

function educational_compare(a, b){
    if (typeof(a) != typeof(b)){
        return false;
    } //the types are equal
    if (typeof(a) != 'object'){
        // they're like... ints or something?
        return a === b;
    } //both are objects
    if (a == null && b == null){
        return true;
    } // two nulls are the same, right?
    if (a == null || b == null){
        return false;
    } // null != non-null
    return (recursive_compare(a, b) && recursive_compare(b,a));
}

