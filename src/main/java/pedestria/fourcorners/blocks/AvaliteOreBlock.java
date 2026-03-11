package pedestria.fourcorners.blocks;


import java.util.Random;

import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.item.Item;

public class AvaliteOreBlock extends ItemDropOreBlock {


	public AvaliteOreBlock(String name, Material material, Item toDrop) {
		super(name, material, toDrop);

		setSoundType(SoundType.METAL);
		setHardness(3.0F);
		setResistance(20.0F);
		setHarvestLevel("pickaxe", 3);
		setLightLevel(7.0F);

	}
	
	@Override
	public int quantityDropped(Random random) {

		int min = 1;
		int max = 2;
		return random.nextInt(max) + min;
	}

}
