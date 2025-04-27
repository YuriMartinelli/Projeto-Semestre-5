import React from "react";
import { Box, Typography, List, ListItem, ListItemText } from "@mui/material";

const FuncionarioList = () => {
    const funcionarios = ["João", "Maria", "Carlos", "Ana"];

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
                Lista de Funcionários
            </Typography>
            <List sx={{ width: "100%", maxWidth: 360, bgcolor: "background.paper" }}>
                {funcionarios.map((funcionario, index) => (
                    <ListItem key={index}>
                        <ListItemText primary={funcionario} />
                    </ListItem>
                ))}
            </List>
        </Box>
    );
};

export default FuncionarioList;