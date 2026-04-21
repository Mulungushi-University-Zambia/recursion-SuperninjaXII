FUNCTION f(n)
    IF n IS 0 OR n IS 1 OR n IS NULL THEN
        RETURN 1
    END IF

    RETURN n * f(n - 1)
END FUNCTION

PRINT f(7)
