import { useForm } from 'react-hook-form';
import {
    TextField,
    Button,
    Box,
    Typography,
    MenuItem,
    FormControl,
    InputLabel,
    Select,
    Toolbar
} from '@mui/material';
const FuncionarioForm = () => {
    const { register, handleSubmit, reset, formState: { errors } } = useForm();
    const onSubmit = (data) => {
        console.log("Dados do funcionário:", data);
    };
    return (
        <Box
            component="form"
            onSubmit={handleSubmit(onSubmit)}
            sx={{
                backgroundColor: '#f0f8ff',
                padding: 4,
                borderRadius: 2,
                boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.1)',
                maxWidth: 600,
                margin: 'auto',
                mt: 4,
            }}
        >
            <Toolbar
                sx={{
                    backgroundColor: '#4682b4',
                    padding: 2,
                    borderRadius: 2,
                    mb: 3,
                    display: 'flex',
                    justifyContent: 'space-between',
                }}
            >
                <Typography variant="h6" color="white">
                    Dados Funcionário
                </Typography>
            </Toolbar>
            <TextField
                label="Nome"
                fullWidth
                margin="normal"
                {...register('nome', { required: 'Nome é obrigatório' })}
                error={!!errors.nome}
                helperText={errors.nome?.message}
                sx={{ backgroundColor: 'white', borderRadius: 1 }}
            />
            <TextField
                label="CPF"
                fullWidth
                margin="normal"
                {...register('cpf', { required: 'CPF é obrigatório' })}
                error={!!errors.cpf}
                helperText={errors.cpf?.message}
                sx={{ backgroundColor: 'white', borderRadius: 1 }}
            />
            <TextField
                label="Matrícula"
                fullWidth
                margin="normal"
                {...register('matricula', { required: 'Matrícula é obrigatória' })}
                error={!!errors.matricula}
                helperText={errors.matricula?.message}
                sx={{ backgroundColor: 'white', borderRadius: 1 }}
            />
            <TextField
                label="Telefone"
                fullWidth
                margin="normal"
                {...register('telefone')}
                sx={{ backgroundColor: 'white', borderRadius: 1 }}
            />
            <TextField
                label="Senha"
                type="password"
                fullWidth
                margin="normal"
                {...register('senha', {
                    required: 'Senha é obrigatória',
                    minLength: { value: 6, message: 'Senha deve ter pelo menos 6 caracteres' },
                })}
                error={!!errors.senha}
                helperText={errors.senha?.message}
                sx={{ backgroundColor: 'white', borderRadius: 1 }}
            />
            <FormControl fullWidth margin="normal" sx={{ backgroundColor: 'white', borderRadius: 1 }}>
                <InputLabel id="grupo-label">Grupo</InputLabel>
                <Select
                    labelId="grupo-label"
                    label="Grupo"
                    onChange={(e) => setGrupo(e.target.value)}
                    {...register('grupo')}
                >
                    <MenuItem value="admin">Admin</MenuItem>
                    <MenuItem value="gerente">Gerente</MenuItem>
                    <MenuItem value="funcionario">Funcionário</MenuItem>
                </Select>
            </FormControl>
            <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 3 }}>
                <Button
                    sx={{
                        mr: 2,
                        backgroundColor: '#d3d3d3',
                        color: '#000',
                        '&:hover': { backgroundColor: '#c0c0c0' },
                    }}
                >
                    Cancelar
                </Button>
                <Button
                    type="submit"
                    variant="contained"
                    sx={{
                        backgroundColor: '#4682b4',
                        color: 'white',
                        '&:hover': { backgroundColor: '#4169e1' },
                    }}
                >
                    Cadastrar
                </Button>
            </Box>
        </Box>
    );
};