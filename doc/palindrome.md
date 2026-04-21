FUNCTION check(word)
    buffer ← empty list
    reversedBuffer ← empty list

    FOR each character i IN word
        append i TO buffer
    END FOR

    reversedBuffer ← reverse(buffer)

    IF reversedBuffer IS EQUAL TO buffer THEN
        RETURN True
    ELSE
        RETURN False
    END IF
END FUNCTION

PRINT check("level")
