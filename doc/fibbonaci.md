FUNCTION f(n)
    IF n IS 0 THEN
        RETURN 0
    ELSE IF n IS 1 THEN
        RETURN 1
    END IF

    RETURN f(n - 1) + f(n - 2)
END FUNCTION

PRINT f(4)
