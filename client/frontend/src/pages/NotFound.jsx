import React from "react";
import { Box, Typography } from "@mui/material";

const NotFound = () => {
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
            <Typography variant="h4" color="error" sx={{ mb: 2 }}>
                404 - Página Não Encontrada
            </Typography>
            <Typography variant="body1" color="textSecondary">
                A página que você está procurando não existe.
            </Typography>
        </Box>
    );
};

export default NotFound;