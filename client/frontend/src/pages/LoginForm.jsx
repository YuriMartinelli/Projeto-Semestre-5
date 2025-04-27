import React from "react";
import { Box, Typography, TextField, Button } from "@mui/material";

const LoginForm = () => {
    return (
        <Box
            sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                minHeight: "100vh",
                backgroundColor: "#f9f9f9",
                padding: 3,
            }}
        >
            <Typography variant="h4" color="primary" sx={{ mb: 3 }}>
                Login
            </Typography>
            <TextField label="Usuário" variant="outlined" sx={{ mb: 2, width: "300px" }} />
            <TextField label="Senha" type="password" variant="outlined" sx={{ mb: 3, width: "300px" }} />
            <Button variant="contained" color="primary" sx={{ width: "300px" }}>
                Entrar
            </Button>
        </Box>
    );
};

export default LoginForm;