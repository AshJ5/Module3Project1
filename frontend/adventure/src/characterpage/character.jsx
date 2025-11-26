import './character.css';
import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import charBlank from '../assets/placeholder/charblank.png';
import wepBlank from '../assets/placeholder/wepblank.png';


function CharacterPage({ characterImg, weaponImg }) {
    const [name, setName] = useState('');
    const [selectedClass, setSelectedClass] = useState('');
    const [selectedWeapon, setSelectedWeapon] = useState('');
    const [classes, setClasses] = useState([]);
    const [availableWeapons, setAvailableWeapons] = useState([]);

    // Fetch classes on mount
    useEffect(() => {
        console.log('Fetching classes...');
        fetch('http://localhost:8000/api/classes')
            .then(res => res.json())
            .then(data => {
                console.log('Classes fetched:', data);
                setClasses(data);
            })
            .catch(error => console.error('Error fetching classes:', error));
    }, []);

    // Fetch weapons when class changes
    useEffect(() => {
        if (selectedClass) {
            fetch(`http://localhost:8000/api/classes/${selectedClass}/weapons`)
                .then(res => res.json())
                .then(data => setAvailableWeapons(data))
                .catch(error => console.error('Error fetching weapons:', error));
        }
    }, [selectedClass]);

    // Compute images based on selections
    const classImage = selectedClass 
        ? classes.find(c => c.id === parseInt(selectedClass))?.icon_path || ''
        : '';
    
    const weaponImage = selectedWeapon
        ? availableWeapons.find(w => w.id === parseInt(selectedWeapon))?.sprite_image || ''
        : '';

    const handleSubmit = (e) => {
        e.preventDefault();
        
        const characterData = {
            name: name,
            class_id: parseInt(selectedClass),
            equipped_weapon_id: parseInt(selectedWeapon)
        };
        
        fetch('http://localhost:8000/api/characters', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(characterData)
        })
        .then(res => {
            if (!res.ok) {
                throw new Error('Failed to create character');
            }
            return res.json();
        })
        .then(data => {
            console.log('Character created:', data);
            alert('Character created successfully!');
            // TODO: Navigate to next page or reset form
        })
        .catch(error => {
            console.error('Error creating character:', error);
            alert('Error creating character. Please try again.');
        });
    };

    return(
        <>
        <Container>
        <Row>
            <Col md={{span: 3}}>
                <img src={characterImg || classImage || charBlank} alt="character" className="character-preview" />
            </Col>
            <Col md={{span: 6}}>
                <img src={weaponImg || weaponImage || wepBlank} alt="weapon" className="weapon-preview" />
            </Col>
        </Row>
        <Row>
            <Col md={{span: 8, offset: 2}}>
                <Form onSubmit={handleSubmit}>
                    <Form.Group className="mb-3">
                        <Form.Label>Character Name</Form.Label>
                        <Form.Control 
                            type="text"
                            placeholder="Enter character name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            maxLength={50}
                            required
                        />
                        <Form.Text className="text-muted">
                            {name.length}/50 characters
                        </Form.Text>
                    </Form.Group>

                    <Form.Group className="mb-3">
                        <Form.Label>Class</Form.Label>
                        <Form.Select 
                            value={selectedClass}
                            onChange={(e) => {
                                setSelectedClass(e.target.value);
                                setSelectedWeapon(''); // Reset weapon when class changes
                            }}
                            required
                        >
                            <option value="">Choose a class...</option>
                            {classes.map(classItem => (
                                <option key={classItem.id} value={classItem.id}>
                                    {classItem.name}
                                </option>
                            ))}
                        </Form.Select>
                    </Form.Group>

                    <Form.Group className="mb-3">
                        <Form.Label>Weapon</Form.Label>
                        <Form.Select 
                            value={selectedWeapon}
                            onChange={(e) => setSelectedWeapon(e.target.value)}
                            disabled={!selectedClass}
                            required
                        >
                            <option value="">Choose a weapon...</option>
                            {availableWeapons.map(weapon => (
                                <option key={weapon.id} value={weapon.id}>
                                    {weapon.name}
                                </option>
                            ))}
                        </Form.Select>
                        {!selectedClass && (
                            <Form.Text className="text-muted">
                                Select a class first
                            </Form.Text>
                        )}
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Create Character
                    </Button>
                </Form>
            </Col>
        </Row>
        </Container>
        </>
    )
} 

export default CharacterPage;